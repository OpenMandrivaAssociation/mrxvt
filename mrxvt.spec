%define name	mrxvt
%define version	0.5.4
%define release	4

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



%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.5.4-3mdv2011.0
+ Revision: 636297
- tighten BR

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.4-2mdv2011.0
+ Revision: 612947
- the mass rebuild of 2010.1 packages

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.5.4-1mdv2010.1
+ Revision: 516421
- update to 0.5.4

* Fri Oct 09 2009 Olivier Blin <oblin@mandriva.com> 0.5.3-5mdv2010.0
+ Revision: 456355
- buildrequire libx11-common to fix build with xim

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.5.3-4mdv2009.1
+ Revision: 350232
- 2009.1 rebuild

* Thu Dec 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-3mdv2009.1
+ Revision: 313212
- lowercase ImageMagick

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.5.3-3mdv2009.0
+ Revision: 253013
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Feb 06 2008 Funda Wang <fwang@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 162927
- update to new version 0.5.3

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Jérôme Soyer <saispo@mandriva.org> 0.5.2-1mdv2008.1
+ Revision: 109361
- New release


* Wed Aug 02 2006 Couriousous <couriousous@mandriva.org> 0.5.1-1mdv2007.0
- 0.5.1
- XDG

* Thu Apr 13 2006 Lenny Cartier <lenny@mandriva.com> 0.5.0-1mdk
- 0.5.0
- remove patch merged upstream

* Wed Nov 16 2005 Lenny Cartier <lenny@mandriva.com> 0.4.2-1mdk
- 0.4.2

* Sun May 08 2005 Couriousous <couriousous@mandriva.org> 0.4.1-1mdk
- 0.4.1
- Fix buildrequires for amd64

* Tue Mar 15 2005 Couriousous <couriousous@mandrake.org> 0.4.0-2mdk
- Reupload

* Tue Mar 01 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.4.0-1mdk
- 0.4.0

* Mon Jan 31 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3.12-2mdk
- patch 0: fix IM support (thus enabling SCIM support in rxvt)

* Sun Jan 23 2005 Couriousous <couriousous@mandrake.orf> 0.3.12-1mdk
- New Release

* Sat Dec 25 2004 Marcel Pol <mpol@mandrake.org> 0.3.11-2mdk
- buildrequires ImageMagick

* Sat Dec 18 2004 Couriousous <couriousous@mandrake.org> 0.3.11-1mdk
- Add menu
- Minors fixs
- Enable more features
- From Lev Givon <lev@columbia.edu>
  - initial Mandrakelinux packaging attempt

