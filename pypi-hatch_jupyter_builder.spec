#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-hatch_jupyter_builder
Version  : 0.8.3
Release  : 1
URL      : https://files.pythonhosted.org/packages/b1/b2/3c304707d4d3c30b2c87f1b8f8b2eb4a682662fea13bd5ab8f16c4c0eb0b/hatch_jupyter_builder-0.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/b2/3c304707d4d3c30b2c87f1b8f8b2eb4a682662fea13bd5ab8f16c4c0eb0b/hatch_jupyter_builder-0.8.3.tar.gz
Summary  : A hatch plugin to help build Jupyter packages
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-hatch_jupyter_builder-bin = %{version}-%{release}
Requires: pypi-hatch_jupyter_builder-license = %{version}-%{release}
Requires: pypi-hatch_jupyter_builder-python = %{version}-%{release}
Requires: pypi-hatch_jupyter_builder-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# hatch-jupyter-builder
[![PyPI - Version](https://img.shields.io/pypi/v/hatch-jupyter-builder.svg)](https://pypi.org/project/hatch-jupyter-builder)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

%package bin
Summary: bin components for the pypi-hatch_jupyter_builder package.
Group: Binaries
Requires: pypi-hatch_jupyter_builder-license = %{version}-%{release}

%description bin
bin components for the pypi-hatch_jupyter_builder package.


%package license
Summary: license components for the pypi-hatch_jupyter_builder package.
Group: Default

%description license
license components for the pypi-hatch_jupyter_builder package.


%package python
Summary: python components for the pypi-hatch_jupyter_builder package.
Group: Default
Requires: pypi-hatch_jupyter_builder-python3 = %{version}-%{release}

%description python
python components for the pypi-hatch_jupyter_builder package.


%package python3
Summary: python3 components for the pypi-hatch_jupyter_builder package.
Group: Default
Requires: python3-core
Provides: pypi(hatch_jupyter_builder)
Requires: pypi(hatchling)

%description python3
python3 components for the pypi-hatch_jupyter_builder package.


%prep
%setup -q -n hatch_jupyter_builder-0.8.3
cd %{_builddir}/hatch_jupyter_builder-0.8.3
pushd ..
cp -a hatch_jupyter_builder-0.8.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693499470
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hatch_jupyter_builder
cp %{_builddir}/hatch_jupyter_builder-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-hatch_jupyter_builder/5369d456ce2bdc5dff0a3003963843b0f0869bf9 || :
cp %{_builddir}/hatch_jupyter_builder-%{version}/tests/data/create_cmdclass/myproject/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-hatch_jupyter_builder/dc2464c1c159acc721e50289b7d609d032d93d22 || :
cp %{_builddir}/hatch_jupyter_builder-%{version}/tests/data/npm_builder/myextension/LICENSE %{buildroot}/usr/share/package-licenses/pypi-hatch_jupyter_builder/4bcc1ca25830d2a662daa02a80fcc421cdced597 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hatch-jupyter-builder

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hatch_jupyter_builder/4bcc1ca25830d2a662daa02a80fcc421cdced597
/usr/share/package-licenses/pypi-hatch_jupyter_builder/5369d456ce2bdc5dff0a3003963843b0f0869bf9
/usr/share/package-licenses/pypi-hatch_jupyter_builder/dc2464c1c159acc721e50289b7d609d032d93d22

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*