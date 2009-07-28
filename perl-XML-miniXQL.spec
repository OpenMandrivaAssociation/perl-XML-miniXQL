%define upstream_name 	 XML-miniXQL
%define upstream_version 0.04

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(XML::Parser)
Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl , perl-XML-Parser

%description
This module provides a simplistic XQL like search engine for XML files.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q  -n %{upstream_name}-%{upstream_version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install

make PREFIX=$RPM_BUILD_ROOT%{_prefix} DESTDIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README MANIFEST Changes 
%{perl_vendorlib}/XML/*
%{perl_vendorlib}/auto/XML/*
%{_mandir}/*/*
