Name:           greaseweazle
Version:        1.22
Release:        1%{?dist}
Summary:        Host tools for controlling a Greaseweazle USB device

License:        Unlicense
URL:            https://github.com/keirf/greaseweazle
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.zip

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
* Sun Jul 27 2025 Dan Horák <dan[at]danny.cz> - 1.22-1
- initial Fedora version
