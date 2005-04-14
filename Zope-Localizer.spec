%define		zope_subname	Localizer
Summary:	A Zope product to develop multilingual web application
Summary(pl):	Dodatek do Zope umożliwiający tworzenie wielojęzycznych aplikacji WWW
Name:		Zope-%{zope_subname}
#%%define		sub_ver b5
Version:	1.1.0
Release:	5
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.ikaaro.org/download/localizer/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	97ba60a9054dd082ecc68c3ab5b1bf8b
URL:		http://www.localizer.org/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope >= 2.7
Requires:	python-itools >= 0.7.3
Requires:	Zope-iHotfix >= 0.5.2
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Localizer is a Zope product to develop multilingual web application.

%description -l pl
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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt Changelog README.txt RELEASE*.txt.en TODO.txt
%lang(es) %doc RELEASE*.txt.es
%lang(fr) %doc RELEASE*.txt.fr
%{_datadir}/%{name}
