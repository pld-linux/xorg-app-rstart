Summary:	rstart and rstartd applications - Remote Start client and helper
Summary(pl.UTF-8):	Aplikacje rstart i rstartd - klient i program do zdalnego uruchamiania
Name:		xorg-app-rstart
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/rstart-%{version}.tar.xz
# Source0-md5:	b7dc8f8532fcf5f846ff22b8a0d88b63
Patch0:		%{name}-configdir.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 1.8
# contexts/x11r6
Requires:	xorg-app-iceauth
# contexts/x11r6, rstart client
Requires:	xorg-app-xauth
# commands/x11r6/LoadMonitor
Requires:	xorg-app-xload
# commands/x11r6/Terminal
Requires:	xterm
Requires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rstart is a simple implementation of a Remote Start client as defined
in "A Flexible Remote Execution Protocol Based on rsh". It uses rsh as
its underlying remote execution mechanism.

rstartd is an implementation of a Remote Start "helper" as defined in
"A Flexible Remote Execution Protocol Based on rsh".

%description -l pl.UTF-8
rstart to prosta implementacja klienta zdalnego uruchamiania (Remote
Start) opisanego w publikacji "A Flexible Remote Execution Protocol
Based on rsh". Wykorzystuje rsh jako mechanizm zdalnego wykonywania.

rstartd to implementacja programu pomocniczego ("helpera") opisanego w
"A Flexible Remote Execution Protocol Based on rsh".

%prep
%setup -q -n rstart-%{version}
%patch0 -p1

# workaround unnecessary AC_CONFIG_MACRO_DIR([m4]) in configure.ac
mkdir m4

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	RSH=/usr/bin/rsh \
	--with-default-man-path="/usr/share/man:/usr/local/man" \
	--with-default-user-path="/usr/local/bin:/usr/bin:/bin"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/rstart
%attr(755,root,root) %{_bindir}/rstartd
%dir %{_libdir}/X11/rstart
%attr(755,root,root) %{_libdir}/X11/rstart/rstartd.real
%{_libdir}/X11/rstart/commands
%{_libdir}/X11/rstart/contexts
%dir /etc/X11/rstart
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/config
%{_mandir}/man1/rstart.1*
%{_mandir}/man1/rstartd.1*
