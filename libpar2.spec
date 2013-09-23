%define major 0
%define beta %{nil}
%define scmrev %{nil}
%define libname %mklibname par2 %{major}
%define devname %mklibname par2 -d

Name: libpar2
Version: 0.2
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 1
Source: http://sourceforge.net/projects/parchive/files/libpar2/%{version}/libpar2-%{version}.tar.gz
%else
Release: 0.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: Library for recovering arbitrary data using parity data
# From nzbget tarball
Patch0: libpar2-0.2-cancel.patch
Patch1: libpar2-0.2-bugfixes.patch
URL: http://sourceforge.net/projects/parchive/files/libpar2/
License: GPL
Group: System/Libraries
BuildRequires: stdc++-devel
BuildRequires: pkgconfig(sigc++-2.0)

%description
Library for recovering arbitrary data using parity data

%package -n %{libname}
Summary: Library for recovering arbitrary data using parity data
Group: System/Libraries

%description -n %{libname}
Library for recovering arbitrary data using parity data

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif
%apply_patches
libtoolize --force
autoreconf -f
%configure

%build
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/%{name}
%{_libdir}/*.so
