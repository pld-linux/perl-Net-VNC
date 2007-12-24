#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	VNC
Summary:	Net::VNC - a simple VNC client
Summary(pl.UTF-8):	Net::VNC - prosty klient VNC
Name:		perl-Net-VNC
Version:	0.36
Release:	0.1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f53dd587c17155622f64db9020c892b0
URL:		http://search.cpan.org/dist/Net-VNC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual Network Computing (VNC) is a desktop sharing system which uses
the RFB (Remote FrameBuffer) protocol to remotely control another
computer. This module acts as a VNC client and communicates to a VNC
server using the RFB protocol, allowing you to capture the screen of
the remote computer. This module dies upon connection errors (with a
timeout of 15 seconds) and protocol errors. This implementation is
based largely on the RFB Protocol Specification,
<http://www.realvnc.com/docs/rfbproto.pdf>. That document has an error
in the DES encryption description, which is clarified via
<http://www.vidarholen.net/contents/junk/vnc.html>.

%description -l pl.UTF-8
VNC (Virtual Network Computing) to system współdzielenia pulpitu
używający protokołu RFB (Remote FrameBuffer - zdalnego framebuffera)
do zdalnego sterowania innym komputerem. Ten moduł działa jako klient
VNC, komunikując się z serwerem VNC przy użyciu protokołu RFB,
pozwalając na przechwytywanie ekranu zdalnego komputera. Moduł umiera
przy błędach połączenia (z timeoutem 15 sekund) i błędach protokołu.
Ta implementacja jest oparta głównie na specyfikacji protokołu RFB
<http://www.realvnc.com/docs/rfbproto.pdf>. Dokument ten zawiera błąd
w opisie szyfrowania DES, wyjaśniony pod
<http://www.vidarholen.net/contents/junk/vnc.html>.

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
%doc CHANGES README
%attr(755,root,root) %{_bindir}/vnccapture
%{perl_vendorlib}/Net/VNC.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
