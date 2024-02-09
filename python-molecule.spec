# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-molecule
Epoch: 100
Version: 24.6.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Molecule aids in the development and testing of Ansible roles
License: MIT
URL: https://github.com/ansible-community/molecule/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-click-help-colors >= 0.9
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Molecule project is designed to aid in the development and testing of
Ansible roles. Molecule provides support for testing with multiple
instances, operating systems and distributions, virtualization
providers, test frameworks and testing scenarios. Molecule encourages an
approach that results in consistently developed roles that are
well-written, easily understood and maintained.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -Dpm644 asset/bash_completion/molecule.bash-completion.sh %{buildroot}%{_datadir}/bash-completion/completions/molecule
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-molecule
Summary: Molecule aids in the development and testing of Ansible roles
Requires: ansible-core >= 2.12.10
Requires: python3
Requires: python3-Jinja2 >= 2.11.3
Requires: python3-PyYAML >= 5.1
Requires: python3-ansible-compat >= 4.1.8
Requires: python3-click >= 8.0
Requires: python3-click-help-colors >= 0.9
Requires: python3-cookiecutter >= 1.7.3
Requires: python3-enrich >= 1.2.7
Requires: python3-jsonschema >= 4.9.1
Requires: python3-packaging
Requires: python3-pluggy >= 0.7.1
Requires: python3-rich >= 9.5.1
Provides: python3-molecule = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-molecule
Molecule project is designed to aid in the development and testing of
Ansible roles. Molecule provides support for testing with multiple
instances, operating systems and distributions, virtualization
providers, test frameworks and testing scenarios. Molecule encourages an
approach that results in consistently developed roles that are
well-written, easily understood and maintained.

%files -n python%{python3_version_nodots}-molecule
%license LICENSE
%{_bindir}/*
%{_datadir}/bash-completion/completions/molecule
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-molecule
Summary: Molecule aids in the development and testing of Ansible roles
Requires: ansible-core >= 2.12.10
Requires: python3
Requires: python3-ansible-compat >= 4.1.8
Requires: python3-click >= 8.0
Requires: python3-click-help-colors >= 0.9
Requires: python3-cookiecutter >= 1.7.3
Requires: python3-enrich >= 1.2.7
Requires: python3-Jinja2 >= 2.11.3
Requires: python3-jsonschema >= 4.9.1
Requires: python3-packaging
Requires: python3-pluggy >= 0.7.1
Requires: python3-PyYAML >= 5.1
Requires: python3-rich >= 9.5.1
Provides: python3-molecule = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule) = %{epoch}:%{version}-%{release}

%description -n python3-molecule
Molecule project is designed to aid in the development and testing of
Ansible roles. Molecule provides support for testing with multiple
instances, operating systems and distributions, virtualization
providers, test frameworks and testing scenarios. Molecule encourages an
approach that results in consistently developed roles that are
well-written, easily understood and maintained.

%files -n python3-molecule
%license LICENSE
%{_bindir}/*
%{_datadir}/bash-completion/completions/molecule
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-molecule
Summary: Molecule aids in the development and testing of Ansible roles
Requires: ansible-core >= 2.12.10
Requires: python3
Requires: python3-ansible-compat >= 4.1.8
Requires: python3-click >= 8.0
Requires: python3-click-help-colors >= 0.9
Requires: python3-cookiecutter >= 1.7.3
Requires: python3-enrich >= 1.2.7
Requires: python3-jinja2 >= 2.11.3
Requires: python3-jsonschema >= 4.9.1
Requires: python3-packaging
Requires: python3-pluggy >= 0.7.1
Requires: python3-pyyaml >= 5.1
Requires: python3-rich >= 9.5.1
Provides: python3-molecule = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule) = %{epoch}:%{version}-%{release}

%description -n python3-molecule
Molecule project is designed to aid in the development and testing of
Ansible roles. Molecule provides support for testing with multiple
instances, operating systems and distributions, virtualization
providers, test frameworks and testing scenarios. Molecule encourages an
approach that results in consistently developed roles that are
well-written, easily understood and maintained.

%files -n python3-molecule
%license LICENSE
%{_bindir}/*
%{_datadir}/bash-completion/completions/molecule
%{python3_sitelib}/*
%endif

%changelog
