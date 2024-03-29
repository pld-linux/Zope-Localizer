%define		zope_subname	Localizer
Summary:	A Zope product to develop multilingual web application
Summary(pl.UTF-8):	Dodatek do Zope umożliwiający tworzenie wielojęzycznych aplikacji WWW
Name:		Zope-%{zope_subname}
Version:	1.2.3
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://download.ikaaro.org/localizer/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	5978c8192106ee77e9d4bd5f992a68e4
URL:		http://www.localizer.org/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope >= 2.7
Requires:	Zope-iHotfix >= 0.5.2
Requires:	python-itools >= 0.9.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Localizer is a Zope product to develop multilingual web application.

%description -l pl.UTF-8
Localizer jest dodatkiem do Zope umożliwiającym tworzenie
wielojęzycznych aplikacji WWW.

%prep
%setup -q -n %{zope_subname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {help,img,locale,tests,ui,*.py,*.gif,*.jpg,charsets.txt,version.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE-* TODO.txt
%{_datadir}/%{name}
