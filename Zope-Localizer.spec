%include	/usr/lib/rpm/macros.python
%define		zope_subname	Localizer
Summary:	Localizer - a Zope product to develop multilingual web application
Summary(pl):	Localizer - dodatek do Zope umo¿liwiaj±cy tworzenie wielojêzycznych aplikacji WWW
Name:		Zope-%{zope_subname}
%define		sub_ver a2
Version:	1.1.0
Release:	2.%{sub_ver}
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/lleu/%{zope_subname}-%{version}%{sub_ver}.tgz
# Source0-md5:	7d2f33fe81c1c9dd554ed3fcfa5dbb4d
URL:		http://www.localizer.org/
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	python-itools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
Localizer is a Zope product to develop multilingual web application.

%description -l pl
Localizer jest dodatkiem do Zope umo¿liwiaj±cym tworzenie
wielojêzycznych aplikacji WWW.

%prep
%setup -q -c %{zope_subname}-%{version}%{sub_ver}

%build
cd %{zope_subname}
mkdir docs
mv -f BUGS.txt INSTALL.txt README.txt RELEASE* TODO.txt docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}

cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/docs/*
%{product_dir}/%{zope_subname}
