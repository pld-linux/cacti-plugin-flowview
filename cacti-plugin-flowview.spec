# TODO
# - bundles external Open Flash Chart - PHP libraries
%define		plugin flowview
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti -  Flowview
Summary(pl.UTF-8):	Wtyczka do Cacti -  Flowview
Name:		cacti-plugin-%{plugin}
Version:	1.1
Release:	8
License:	GPL
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{version}-1.tgz
# Source0-md5:	e165e0d4cb68c1033bae131a67c89967
URL:		http://docs.cacti.net/plugin:flowview
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.0
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

# bad depsolver
# pear JSON will not be needed, we R json ext
%define		_noautopear	pear pear(JSON.php)

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Plugin for Cacti - This plugin allows you to see reports based off the
data in your Netflow flows.

%description -l pl.UTF-8
Wtyczka do Cacti pozwalająca oglądać raporty w oparciu o dane z
przepływów Netflow.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
