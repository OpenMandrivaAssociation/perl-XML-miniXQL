%define module 	XML-miniXQL
%define version 0.04
%define release %mkrel 8

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel perl(XML::Parser)
Requires:	perl , perl-XML-Parser
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
This module provides a simplistic XQL like search engine for XML files.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q  -n %{module}-%{version}

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




