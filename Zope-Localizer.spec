%define		zope_subname	Localizer
Summary:	A Zope product to develop multilingual web application
Summary(pl):	Dodatek do Zope umo¿liwiaj±cy tworzenie wielojêzycznych aplikacji WWW
Name:		Zope-%{zope_subname}
%define		sub_ver b1
Version:	1.1.0
Release:	4.%{sub_ver}.2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/lleu/%{zope_subname}-%{version}%{sub_ver}.tar.gz
# Source0-md5:	71bad7a668db294c60af01da1fe236b6
URL:		http://www.localizer.org/
BuildRequires:	python >= 2.1
%pyrequires_eq	python-modules
Requires:	Zope >= 2.6
Requires:	python-itools >= 0.4
Requires:	Zope-iHotfix >= 0.4
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Localizer is a Zope product to develop multilingual web application.

%description -l pl
Localizer jest dodatkiem do Zope umo¿liwiaj±cym tworzenie
wielojêzycznych aplikacji WWW.

%prep
%setup -q -n %{zope_subname}

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
%doc Changelog README.txt RELEASE*.txt RELEASE*.txt.en TODO.txt old/*.txt INSTALL.txt
%lang(es) %doc RELEASE*.txt.es
%lang(fr) %doc RELEASE*.txt.fr
%{_datadir}/%{name}
