#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	VNC
Summary:	Net::VNC - a simple VNC client
Summary(pl):	Net::VNC - prosty klient VNC
Name:		perl-Net-VNC
Version:	0.35
Release:	0.1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c07b849083955235dfe986148b14db14
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

%description -l pl
VNC (Virtual Network Computing) to system wspó³dzielenia pulpitu
u¿ywaj±cy protoko³u RFB (Remote FrameBuffer - zdalnego framebuffera)
do zdalnego sterowania innym komputerem. Ten modu³ dzia³a jako klient
VNC, komunikuj±c siê z serwerem VNC przy u¿yciu protoko³u RFB,
pozwalaj±c na przechwytywanie ekranu zdalnego komputera. Modu³ umiera
przy b³êdach po³±czenia (z timeoutem 15 sekund) i b³êdach protoko³u.
Ta implementacja jest oparta g³ównie na specyfikacji protoko³u RFB
<http://www.realvnc.com/docs/rfbproto.pdf>. Dokument ten zawiera b³±d
w opisie szyfrowania DES, wyja¶niony pod
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
