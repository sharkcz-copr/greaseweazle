Name:           greaseweazle
Version:        1.23
Release:        2%{?dist}
Summary:        Host tools for controlling a Greaseweazle USB device

License:        Unlicense
URL:            https://github.com/keirf/greaseweazle
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.zip
# https://github.com/misterblack1/greaseweazle
Patch0:         %{name}-diag.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  systemd-devel


%description
Tools for accessing a floppy drive at the raw flux level.


%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{name}

install -D -p -m 644 scripts/49-greaseweazle.rules %{buildroot}/%{_udevrulesdir}/49-greaseweazle.rules


%check


%files -f %{pyproject_files}
%license COPYING
%doc README RELEASE_NOTES
%{_bindir}/gw
%{_udevrulesdir}/49-greaseweazle.rules


%changelog
* Sun Aug 09 2026 Dan Horák <dan[at]danny.cz> - 1.23-2
- add diag tool from https://github.com/misterblack1/greaseweazle

* Thu Jun 25 2026 Dan Horák <dan[at]danny.cz> - 1.23-1
- updated to 1.23

* Sun Jul 27 2025 Dan Horák <dan[at]danny.cz> - 1.22-1
- initial Fedora version
