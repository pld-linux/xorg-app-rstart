Summary:	rstart application
Summary(pl):	Aplikacja rstart
Name:		xorg-app-rstart
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/rstart-%{version}.tar.bz2
# Source0-md5:	b5dd5f0df7eb8295a0957a9739a23123
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rstart application.

%description -l pl
Aplikacja rstart.

%prep
%setup -q -n rstart-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/X11/rstart
%{_libdir}/X11/rstart/commands
%{_libdir}/X11/rstart/config
%{_libdir}/X11/rstart/contexts
%attr(755,root,root) %{_libdir}/X11/rstart/rstartd.real
%{_mandir}/man1/*.1x*
