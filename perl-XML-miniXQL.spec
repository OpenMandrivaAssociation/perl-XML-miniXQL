%define upstream_name 	 XML-miniXQL
%define upstream_version 0.04
Name:		perl-%{upstream_name}
Version:	0.04
Release:	1

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-miniXQL
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/XML-miniXQL-0.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch
Requires:	perl(XML::Parser)

%description
This module provides a simplistic XQL like search engine for XML files.

%prep
%setup -q  -n %{upstream_name}-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}

%files 
%doc README MANIFEST Changes 
%{perl_vendorlib}/XML/*
%{perl_vendorlib}/auto/XML/*
%{_mandir}/*/*


