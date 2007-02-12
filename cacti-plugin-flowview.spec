%define		namesrc	 flowview
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti -  Flowview
Summary(pl.UTF-8):	Wtyczka do Cacti -  Flowview
Name:		cacti-plugin-flowview
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://cactiusers.net/downloads/plugins/%{namesrc}-%{version}.tar.gz
# Source0-md5:	1460ccd8e298401c803b8d472d3c0177
URL:		http://www.cactiusers.org/
#BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - This plugin allows you to see reports based off
the data in your Netflow flows.

%description -l pl.UTF-8
Wtyczka do Cacti pozwalająca oglądać raporty w oparciu o dane z
przepływów Netflow.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
