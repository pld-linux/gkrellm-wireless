Summary:	plugins monitors the signal quality of your wireless networking card
Summary(pl):	plugin monitoruj�cy jako�c sygna�u karty bezprzewodowej
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
This plugins monitors the signal quality of your wireless networking card (if it's driver supports the linux wireless extension api or you use Freebsd's wi0 interface).

%description -l pl
Ten plugin umo�liwia monitorowanie jako�ci sygna�u karty bezprzewodowej.

%prep
%setup -q -n gkrellmwireless

%build
# typo - two different variables for optflags
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -D wireless.so  $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/wireless.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/wireless.so