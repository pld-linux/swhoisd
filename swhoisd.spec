Summary:	Simple WHOIS Daemon for the whois directory service
Summary(pl.UTF-8):	Prosty demon WHOIS dla usługi katalogowej whois
Name:		swhoisd
Version:	3.0.5
Release:	1
License:	BSD-like
Group:		Utilities/Network
Source0:	ftp://dan.drydog.com/pub/swhoisd/%{name}-%{version}.tar.gz
# Source0-md5:	ca534c68541c7de104550924ee440b80
Patch0:		%{name}-select_user.patch
URL:		http://dan.drydog.com/swhoisd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
swhoisd is a simple whois daemon that provides a whois directory
service. It is much simpler to setup and administrator than the other
whois daemons available, such as RIPE whois or the original SRC whois.
This is because it uses a flat-text file over a complex database. This
whois server is recommended only for small databases (preferably under
200 records and no more than 1000).

This daemon conforms to RFC 834 and uses TCP port 43 (service
"whois").

%description -l pl.UTF-8
swhoisd to prosty demon whois dostarczający usługę katalogową whois.
Jest dużo prostszy do skonfigurowania niż inne dostępne demony whois,
jak na przykład RIPE whois czy oryginalny SRC whois. Jest tak ponieważ
swhoisd używa płaskiego pliku tekstowego zamiast złożonej bazy danych.
Ten serwer whois jest zalecany tylko dla małych baz (najlepiej poniżej
200 rekordów, zdecydowanie nie więcej niż 1000).

Ten demon jest zgodny z RFC 834 i używa portu 43 TCP (usługi "whois").

%prep
%setup -q
chmod -R u+rw *
%patch0 -p1 

%build
%{__gettextize}
%{__autoconf}
%{__aclocal}
%{__automake}
%configure \
	--with-user=daemon \
	--with-group=daemon

%{__make}
#cd src
#make
#cd ../doc
#make in.swhoisd.txt
#cd ../po
#make
#make es.mo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,%{_mandir}/man8,%{_sbindir},%{_datadir}/locale/es/LC_MESSAGES}

install -m644 src/swhoisd	$RPM_BUILD_ROOT/etc/rc.d/init.d
install -m644 doc/swhoisd.conf.sample $RPM_BUILD_ROOT/etc/swhoisd.conf
install -m644 doc/swhoisd.header 	$RPM_BUILD_ROOT/etc
install -m644 doc/swhoisd.footer 	$RPM_BUILD_ROOT/etc
#install -m644 doc/whois.xinetd	$RPM_BUILD_ROOT/etc/xinetd.d/whois
install -m644 doc/in.swhoisd.8	$RPM_BUILD_ROOT%{_mandir}/man8
install -m755 src/in.swhoisd	$RPM_BUILD_ROOT%{_sbindir}
install -m644 po/es.mo %{_datadir}/locale/es/LC_MESSAGES/swhoisd.mo

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README THANKS TODO doc/rfc1834.txt
#%doc doc/swhoisd.conf.sample doc/whois.php
#%config(noreplace) /etc/swhoisd.conf
#%config(noreplace) /etc/swhoisd.header
#%config(noreplace) /etc/swhoisd.footer
##%config /etc/xinetd.d/whois
#%attr(754,root,root) /etc/rc.d/init.d/swhoisd
#%attr(755,root,root) %{_sbindir}/in.swhoisd
#%{_mandir}/man8/in.swhoisd.8*
