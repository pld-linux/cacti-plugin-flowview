%define		namesrc	 flowview
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti -  Flowview
Summary(pl):	Wtyczka do Cacti -  Flowview
Name:		cacti-plugin-flowview
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://download.cactiusers.org/downloads/%{namesrc}-%{version}.tar.gz
# Source0-md5:	b2b9cacd33268972d01a3800984e51f8
URL:		http://www.cactiusers.org/
#BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - This plugin allows you to see reports based off
the data in your Netflow flows.

%description -l pl
Wtyczka do Cacti dodaj±ca mo¿liwo¶æ ...

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
