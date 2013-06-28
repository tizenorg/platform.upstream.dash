Name:           dash
Version:        0.5.7
Release:        4
Summary:        Small and fast POSIX-compliant shell
Group:          System/Shells
License:        BSD and GPLv2+
URL:            http://gondor.apana.org.au/~herbert/dash/
Source0:        http://gondor.apana.org.au/~herbert/dash/files/dash-%{version}.tar.gz
Source1001: 	dash.manifest

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as
possible. It does this without sacrificing speed where possible. In fact, it is
significantly faster than bash (the GNU Bourne-Again SHell) for most tasks.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/bin
mv %{buildroot}%{_bindir}/dash %{buildroot}/bin/
rm -rf %{buildroot}%{_bindir}/

%post
grep -q '^/bin/dash$' /etc/shells || echo '/bin/dash' >> /etc/shells

%postun
if [ $1 -eq 0 ]; then
    sed -i '/^\/bin\/dash$/d' /etc/shells
fi

%files
%manifest %{name}.manifest
%doc  COPYING
/bin/dash
%{_datadir}/man/man1/dash.1.gz

