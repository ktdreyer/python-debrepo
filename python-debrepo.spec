%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%if 0%{?fedora}
%global with_python3 1
%endif

%define srcname debrepo

Name:           python-%{srcname}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Inspect and compare Debian repositories
License:        GPLv3+
URL:            https://pagure.io/debrepo
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz


BuildRequires:  python-devel >= 2.6
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # with_python3

BuildArch:      noarch


%description
debrepo is a library for inspecting composes of Debian repositories and
their elements, including package archives. It includes classes capable
of reading compose, repository, and package data from the filesystem,
and methods to compare the data between different versions. To this end,
the debrepodiff tool provides a command line interface for comparing
composes.

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
Requires:       python-debian

%description -n python2-%{srcname}
debrepo is a library for inspecting composes of Debian repositories and
their elements, including package archives. It includes classes capable
of reading compose, repository, and package data from the filesystem,
and methods to compare the data between different versions. To this end,
the debrepodiff tool provides a command line interface for comparing
composes.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3
Requires:       python3-debian
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
debrepo is a library for inspecting composes of Debian repositories and
their elements, including package archives. It includes classes capable
of reading compose, repository, and package data from the filesystem,
and methods to compare the data between different versions. To this end,
the debrepodiff tool provides a command line interface for comparing
composes.
%endif # with_python3

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%{py2_build}

%if 0%{?with_python3}
%{py3_build}
%endif # with_python3

%install
%py2_install
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python2|' \
   %{buildroot}%{_bindir}/debrepodiff

%if 0%{?with_python3}
rm %{buildroot}%{_bindir}/debrepodiff
%py3_install
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
   %{buildroot}%{_bindir}/debrepodiff
%endif # with_python3

%files -n python2-%{srcname}
%doc README.rst
# https://pagure.io/debrepo/pull-request/1
#%%license GPL
%{python_sitelib}/*
%if ! 0%{?with_python3}
%{_bindir}/debrepodiff
%endif

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc README.rst
# https://pagure.io/debrepo/pull-request/1
#%%license GPL
%{python3_sitelib}/*
%{_bindir}/debrepodiff
%endif # with_python3


%changelog
* Mon Mar 13 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.1-1
- initial package
