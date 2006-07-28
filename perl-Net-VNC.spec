#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	VNC
Summary:	perl(Net::VNC) − A simple VNC client
Name:		perl-Net-VNC
Version:	0.35
Release:	0.1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c07b849083955235dfe986148b14db14
URL:		http://search.cpan.org/dist/Net-VNC
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
# none yet
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual Network Computing (VNC) is a desktop sharing system which uses the RFB
(Remote FrameBuffer) protocol to remotely control another computer. This module
acts as a VNC client and communicates to a VNC server using the RFB protocol,
allowing you to capture the screen of the remote computer.
This module dies upon connection errors (with a timeout of 15 seconds) and
protocol errors.  This implementation is based largely on the RFB Protocol
Specification, <http://www.realvnc.com/docs/rfbproto.pdf>. 
That document has an error in the DES encryption description, which is
clarified via <http://www.vidarholen.net/contents/junk/vnc.html>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/vnccapture
%doc CHANGES README
%{perl_vendorlib}/Net/VNC.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
