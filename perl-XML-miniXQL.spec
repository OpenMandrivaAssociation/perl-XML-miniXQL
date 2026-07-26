%define upstream_name 	 XML-miniXQL
Name:		perl-%{upstream_name}
Version:	0.04
Release:	6

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-miniXQL
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/XML-miniXQL-%{version}.tar.gz

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


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 401858
- rebuild using %0.04 Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-11mdv2009.0
+ Revision: 258843
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-10mdv2009.0
+ Revision: 246751
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.04-8mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-8mdv2007.0
+ Revision: 73447
- Fix Build
- Fix URL
- import perl-XML-miniXQL-0.04-7mdk

* Wed Jun 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.04-7mdk
- rebuild

