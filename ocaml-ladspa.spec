Name:     ocaml-ladspa

Version:  0.1.5
Release:  1
Summary:  OCaml bindings for ladspa
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-ladspa
Source0:  https://github.com/savonet/ocaml-ladspa/releases/download/%{version}/ocaml-ladspa-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ladspa-devel
Requires:      ladspa

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/ladspa/META
/usr/lib64/ocaml/ladspa/ladspa.a
/usr/lib64/ocaml/ladspa/ladspa.cma
/usr/lib64/ocaml/ladspa/ladspa.cmi
/usr/lib64/ocaml/ladspa/ladspa.cmxa
/usr/lib64/ocaml/ladspa/ladspa.mli
/usr/lib64/ocaml/ladspa/ladspa.cmx
/usr/lib64/ocaml/ladspa/ocaml_ladspa.h
/usr/lib64/ocaml/ladspa/libladspa_stubs.a
/usr/lib64/ocaml/stublibs/dllladspa_stubs.so
/usr/lib64/ocaml/stublibs/dllladspa_stubs.so.owner

%description
OCAML bindings for ladspa


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-ladspa.spec
