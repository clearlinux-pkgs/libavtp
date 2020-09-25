#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libavtp
Version  : 0.1.0
Release  : 4
URL      : https://github.com/Avnu/libavtp/archive/v0.1.0/libavtp-0.1.0.tar.gz
Source0  : https://github.com/Avnu/libavtp/archive/v0.1.0/libavtp-0.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libavtp-lib = %{version}-%{release}
Requires: libavtp-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(cmocka)

%description
[![Build Status](https://travis-ci.org/AVnu/libavtp.svg?branch=master)](https://travis-ci.org/AVnu/libavtp)

%package dev
Summary: dev components for the libavtp package.
Group: Development
Requires: libavtp-lib = %{version}-%{release}
Provides: libavtp-devel = %{version}-%{release}
Requires: libavtp = %{version}-%{release}

%description dev
dev components for the libavtp package.


%package lib
Summary: lib components for the libavtp package.
Group: Libraries
Requires: libavtp-license = %{version}-%{release}

%description lib
lib components for the libavtp package.


%package license
Summary: license components for the libavtp package.
Group: Default

%description license
license components for the libavtp package.


%prep
%setup -q -n libavtp-0.1.0
cd %{_builddir}/libavtp-0.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601065410
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libavtp
cp %{_builddir}/libavtp-0.1.0/LICENSE %{buildroot}/usr/share/package-licenses/libavtp/b92defa3ef81e1ff1a014f3e0a40e38f0a7f67a7
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/avtp.h
/usr/include/avtp_aaf.h
/usr/include/avtp_crf.h
/usr/include/avtp_cvf.h
/usr/include/avtp_ieciidc.h
/usr/lib64/pkgconfig/avtp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libavtp.so
/usr/lib64/libavtp.so.0
/usr/lib64/libavtp.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libavtp/b92defa3ef81e1ff1a014f3e0a40e38f0a7f67a7
