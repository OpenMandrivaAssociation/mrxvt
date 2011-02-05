%define name	mrxvt
%define version	0.5.4
%define release	%mkrel 3

Summary:	A multi-tabbed X terminal emulator based on rxvt
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Terminals
Url:		http://materm.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libice-devel
BuildRequires:	libsm-devel
BuildRequires:	libx11-devel
BuildRequires:	libxft-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxrender-devel
BuildRequires:	fontconfig-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
# X11 locales are required to build IM support
BuildRequires:	libx11-common
BuildRequires:	imagemagick

%description
Mrxvt is a lightweight and powerful multi-tabbed X terminal emulator based on
the popular emulators rxvt and aterm. It implements many useful features seen
in modern X terminal emulators such as gnome-terminal and konsole while
remaining lightweight and independent of the GNOME and KDE desktop
environments.

%prep
%setup -q

%build
%configure2_5x --disable-debug --enable-keepscrolling --enable-selectionscrolling  --enable-mousewheel --enable-24bits --enable-text-shado --enable-smart-resize --enable-xft --enable-xim --enable-greek --enable-cjk
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}/usr/share/doc/mrxvt

# menu entries

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Mrxvt
Comment=A multi-tabbed X terminal emulator
Exec=/usr/bin/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=TerminalEmulator;System;
EOF


install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}

convert -resize 48x48 share/pixmaps/mrxvt.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -resize 16x16 share/pixmaps/mrxvt.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert -resize 32x32 share/pixmaps/mrxvt.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README TODO ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%{_datadir}/applications/*

