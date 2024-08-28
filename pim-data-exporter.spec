#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : pim-data-exporter
Version  : 24.08.0
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.08.0/src/pim-data-exporter-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/pim-data-exporter-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/pim-data-exporter-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Import and export KDE PIM settings
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: pim-data-exporter-bin = %{version}-%{release}
Requires: pim-data-exporter-data = %{version}-%{release}
Requires: pim-data-exporter-lib = %{version}-%{release}
Requires: pim-data-exporter-license = %{version}-%{release}
Requires: pim-data-exporter-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-notes-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : mailcommon-dev
BuildRequires : messagelib-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

%package bin
Summary: bin components for the pim-data-exporter package.
Group: Binaries
Requires: pim-data-exporter-data = %{version}-%{release}
Requires: pim-data-exporter-license = %{version}-%{release}

%description bin
bin components for the pim-data-exporter package.


%package data
Summary: data components for the pim-data-exporter package.
Group: Data

%description data
data components for the pim-data-exporter package.


%package doc
Summary: doc components for the pim-data-exporter package.
Group: Documentation

%description doc
doc components for the pim-data-exporter package.


%package lib
Summary: lib components for the pim-data-exporter package.
Group: Libraries
Requires: pim-data-exporter-data = %{version}-%{release}
Requires: pim-data-exporter-license = %{version}-%{release}

%description lib
lib components for the pim-data-exporter package.


%package license
Summary: license components for the pim-data-exporter package.
Group: Default

%description license
license components for the pim-data-exporter package.


%package locales
Summary: locales components for the pim-data-exporter package.
Group: Default

%description locales
locales components for the pim-data-exporter package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n pim-data-exporter-24.08.0
cd %{_builddir}/pim-data-exporter-24.08.0
pushd ..
cp -a pim-data-exporter-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724697933
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724697933
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pim-data-exporter
cp %{_builddir}/pim-data-exporter-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/pim-data-exporter-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/pim-data-exporter-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/pim-data-exporter-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/pim-data-exporter-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/pim-data-exporter-%{version}/gui/org.kde.pimdataexporter.desktop.license %{buildroot}/usr/share/package-licenses/pim-data-exporter/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/pim-data-exporter-%{version}/gui/pimdataexporter.qrc.license %{buildroot}/usr/share/package-licenses/pim-data-exporter/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang pimdataexporter
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pimdataexporter
/V3/usr/bin/pimdataexporterconsole
/usr/bin/pimdataexporter
/usr/bin/pimdataexporterconsole

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.pimdataexporter.desktop
/usr/share/config.kcfg/pimdataexporterglobalconfig.kcfg
/usr/share/metainfo/org.kde.pimdataexporter.appdata.xml
/usr/share/qlogging-categories6/pimdataexporter.categories
/usr/share/qlogging-categories6/pimdataexporter.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/ca/pimsettingexporter/index.docbook
/usr/share/doc/HTML/ca/pimsettingexporter/selection-dialog.png
/usr/share/doc/HTML/de/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/de/pimsettingexporter/index.docbook
/usr/share/doc/HTML/en/pimdataexporter/index.cache.bz2
/usr/share/doc/HTML/en/pimdataexporter/index.docbook
/usr/share/doc/HTML/en/pimdataexporter/selection-dialog.png
/usr/share/doc/HTML/es/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/es/pimsettingexporter/index.docbook
/usr/share/doc/HTML/et/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/et/pimsettingexporter/index.docbook
/usr/share/doc/HTML/it/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/it/pimsettingexporter/index.docbook
/usr/share/doc/HTML/nl/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/nl/pimsettingexporter/index.docbook
/usr/share/doc/HTML/pt/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/pt/pimsettingexporter/index.docbook
/usr/share/doc/HTML/pt_BR/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/pt_BR/pimsettingexporter/index.docbook
/usr/share/doc/HTML/ru/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/ru/pimsettingexporter/index.docbook
/usr/share/doc/HTML/sv/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/sv/pimsettingexporter/index.docbook
/usr/share/doc/HTML/uk/pimsettingexporter/index.cache.bz2
/usr/share/doc/HTML/uk/pimsettingexporter/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpimdataexporterprivate.so.6.2.0
/usr/lib64/libpimdataexporterprivate.so.6
/usr/lib64/libpimdataexporterprivate.so.6.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pim-data-exporter/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/pim-data-exporter/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/pim-data-exporter/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/pim-data-exporter/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/pim-data-exporter/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/pim-data-exporter/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/pim-data-exporter/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f pimdataexporter.lang
%defattr(-,root,root,-)

