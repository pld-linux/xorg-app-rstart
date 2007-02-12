Summary:	rstart application
Summary(pl.UTF-8):	Aplikacja rstart
Name:		xorg-app-rstart
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/rstart-%{version}.tar.bz2
# Source0-md5:	99aea04a27197056368a4431f30f9cdb
Patch0:		%{name}-configdir.patch
Patch1:		%{name}-install.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
# contexts/x11r6
Requires:	xorg-app-iceauth
# contexts/x11r6, rstart client
Requires:	xorg-app-xauth
# commands/x11r6/LoadMonitor
Requires:	xorg-app-xload
# commands/x11r6/Terminal
Requires:	xterm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rstart application.

%description -l pl.UTF-8
Aplikacja rstart.

%prep
%setup -q -n rstart-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	RSH=/usr/bin/rsh \
	--with-default-man-path="/usr/share/man:/usr/local/man" \
	--with-default-user-path="/usr/local/bin:/usr/bin:/bin"

%{__make} \
	configdir=/etc/X11/rstart

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	configdir=/etc/X11/rstart \
	DATA_DIR=/etc/X11/rstart

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/rstart
%attr(755,root,root) %{_bindir}/rstartd
%dir %{_libdir}/X11/rstart
%attr(755,root,root) %{_libdir}/X11/rstart/rstartd.real
%dir /etc/X11/rstart
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/config
%dir /etc/X11/rstart/commands
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/commands/@List
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/commands/ListContexts
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/commands/ListGenericCommands
%dir /etc/X11/rstart/commands/x11r6
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/commands/x11r6/@List
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/commands/x11r6/LoadMonitor
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/commands/x11r6/Terminal
%config(noreplace,missingok) %verify(not link) /etc/X11/rstart/commands/x11
%config(noreplace,missingok) %verify(not link) /etc/X11/rstart/commands/x
%dir /etc/X11/rstart/contexts
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/contexts/@List
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/contexts/default
%config(noreplace) %verify(not md5 mtime size) /etc/X11/rstart/contexts/x11r6
%config(noreplace,missingok) %verify(not link) /etc/X11/rstart/contexts/x11
%config(noreplace,missingok) %verify(not link) /etc/X11/rstart/contexts/x
%{_mandir}/man1/rstart.1x*
%{_mandir}/man1/rstartd.1x*
