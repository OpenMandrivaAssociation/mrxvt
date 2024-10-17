Summary:	A multi-tabbed X terminal emulator based on rxvt
Name:		mrxvt
Version:	0.5.4
Release:	6
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Terminals
Url:		https://materm.sourceforge.net
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	fontconfig-devel
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
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
%makeinstall_std
rm -rf %{buildroot}/usr/share/doc/mrxvt

# menu entries

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Mrxvt
Name[ru]=Mrxvt
Comment=A multi-tabbed X terminal emulator
Comment[ru]=Эмулятор терминала со вкладками
Exec=/usr/bin/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=TerminalEmulator;System;
EOF


install -m 755 -d %{buildroot}%{_miconsdir}
install -m 755 -d %{buildroot}%{_iconsdir}
install -m 755 -d %{buildroot}%{_liconsdir}

convert -resize 48x48 share/pixmaps/mrxvt.png %{buildroot}%{_liconsdir}/%{name}.png
convert -resize 16x16 share/pixmaps/mrxvt.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 share/pixmaps/mrxvt.png %{buildroot}%{_iconsdir}/%{name}.png

%files
%doc AUTHORS COPYING INSTALL NEWS README TODO ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/applications/*
