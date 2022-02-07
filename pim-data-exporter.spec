#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : pim-data-exporter
Version  : 21.12.2
Release  : 38
URL      : https://download.kde.org/stable/release-service/21.12.2/src/pim-data-exporter-21.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.2/src/pim-data-exporter-21.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.2/src/pim-data-exporter-21.12.2.tar.xz.sig
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
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : karchive-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knotifications-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : mailcommon-dev
BuildRequires : messagelib-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

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
%setup -q -n pim-data-exporter-21.12.2
cd %{_builddir}/pim-data-exporter-21.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644246617
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644246617
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pim-data-exporter
cp %{_builddir}/pim-data-exporter-21.12.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/pim-data-exporter/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/pim-data-exporter-21.12.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/pim-data-exporter-21.12.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/pim-data-exporter-21.12.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/pim-data-exporter-21.12.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-data-exporter/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang pimdataexporter

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pimdataexporter
/usr/bin/pimdataexporterconsole

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.pimdataexporter.desktop
/usr/share/config.kcfg/pimdataexporterglobalconfig.kcfg
/usr/share/metainfo/org.kde.pimdataexporter.appdata.xml
/usr/share/qlogging-categories5/pimdataexporter.categories
/usr/share/qlogging-categories5/pimdataexporter.renamecategories

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
/usr/lib64/libpimdataexporterprivate.so.5
/usr/lib64/libpimdataexporterprivate.so.5.19.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pim-data-exporter/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/pim-data-exporter/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/pim-data-exporter/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/pim-data-exporter/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/pim-data-exporter/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f pimdataexporter.lang
%defattr(-,root,root,-)

