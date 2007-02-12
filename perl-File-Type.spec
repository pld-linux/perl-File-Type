#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Type
Summary:	File::Type - determine file type using magic
Summary(pl.UTF-8):   File::Type - określenie typu pliku za pomocą liczb magicznych
Name:		perl-File-Type
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4be3b0b7000b325c60351fcc8a04815d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Type uses magic numbers (typically at the start of a file) to
determine the MIME type of that file.

File::Type can use either a filename, or file contents, to determine
the type of a file.

%description -l pl.UTF-8
File::Type służy do określania typu MIME pliku za pomocą liczb
magicznych (zazwyczaj zawartych na początku pliku).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/*.pm
%{perl_vendorlib}/File/Type
%{_mandir}/man3/*
