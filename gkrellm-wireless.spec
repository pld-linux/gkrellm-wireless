Summary:	Plugin monitoring the signal quality of your wireless networking card
Summary(pl):	Wtyczka monitoruj±ca jako¶æ sygna³u karty bezprzewodowej
Name:		gkrellm-wireless
Version:	2.0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gkrellm.luon.net/files/gkrellmwireless-%{version}.tar.gz
# Source0-md5:	42ee66a43eb3da5af9f13d3d10d354f6
URL:		http://gkrellm.luon.net/gkrellmwireless.phtml
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin monitors the signal quality of your wireless networking
card (if it's driver supports the Linux wireless extension API).

%description -l pl
Ta wtyczka umo¿liwia monitorowanie jako¶ci sygna³u karty
bezprzewodowej (je¶li jej sterownik obs³uguje linuksowe rozszerzenie
API dla kart bezprzewodowych).

%prep
%setup -q -n gkrellmwireless

%build
%{__make} \
	CC="%{__cc} \$(FLAGS)" \
	FLAGS="%{rpmcflags} -Wall -fPIC \$(GTK_CFLAGS) \$(GKRELLM_INCLUDE)"

%install
rm -rf $RPM_BUILD_ROOT

install -D wireless.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/wireless.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/wireless.so
