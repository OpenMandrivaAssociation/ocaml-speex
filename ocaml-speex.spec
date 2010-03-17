Name:           ocaml-speex
Version:        0.1.2
Release:        %mkrel 1
Summary:        OCaml interface to the speex library
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-speex/ocaml-speex-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ogg-devel
BuildRequires:  libogg-devel
BuildRequires:  libspeex-devel
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
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/speex
make install

%clean
rm -rf %{buildroot}

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

