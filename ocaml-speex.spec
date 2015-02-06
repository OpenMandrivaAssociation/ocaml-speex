Name:           ocaml-speex
Version:        0.1.2
Release:        3
Summary:        OCaml interface to the speex library
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-speex/ocaml-speex-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ogg-devel
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(speex)
Requires:       speex

%description
This package provides an interface to the speex library for 
OCaml programmers.

Speex is an audio codec especially designed for compressing voice at low
bit-rates for applications such as voice over IP (VoIP).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
make
make doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/speex
make install

%files
%defattr(-,root,root)
%doc COPYING README CHANGES
%dir %{_libdir}/ocaml/speex
%{_libdir}/ocaml/speex/META
%{_libdir}/ocaml/speex/*.cma
%{_libdir}/ocaml/speex/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%doc examples
%{_libdir}/ocaml/speex/*.a
%{_libdir}/ocaml/speex/*.cmxa
%{_libdir}/ocaml/speex/*.cmx
%{_libdir}/ocaml/speex/*.mli



%changelog
* Wed Mar 17 2010 Florent Monnier <blue_prawn@mandriva.org> 0.1.2-1mdv2010.1
+ Revision: 522810
- update to new version 0.1.2

* Mon Sep 07 2009 Florent Monnier <blue_prawn@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 432953
- BuildRequires: libogg-devel
- BuildRequires: ocaml-ogg-devel
- BuildRequires: libspeex
- import ocaml-speex

