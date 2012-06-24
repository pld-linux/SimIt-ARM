Summary:	Very fast functional and cycle-accurate simulators for ARM
Summary(pl):	Bardzo szybkie funkcjonalne i dok�adne co do cyklu symulatory ARM-a
Name:		SimIt-ARM
Version:	2.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/simit-arm/%{name}-%{version}.tar.gz
# Source0-md5:	8dfdc17adfccd61de5a0718ebf7c557a
URL:		http://simit-arm.sourceforge.net/
BuildRequires:	byacc
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	libtool
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*nwfpe.bin

%description
SimIt-ARM was developed to demonstrate the usefulness of the Operation
State Machine (OSM) model and the Mescal Architecture Description
Language (MADL). The package contains an instruction-set simulator
(sometimes called emulator) and a cycle-accurate simulator for the
StrongARM architecture. Both simulators read ELF32 little-endian
ARM-linux binaries and can simulate most of the SPEC Int and SPEC FP
benchmarks.

%description -l pl
SimIt-ARM powsta� do demonstracji przydatno�ci modelu OSM (Operation
State Machine - automatu operacji) oraz j�zyka MADL (Mescal
Architecture Description Language). Pakiet zawiera symulator zestawu
instrukcji (czasem zwany emulatorem) oraz dok�adny co do cyklu
symulator architektury StrongARM. Oba symulatory czytaj� binaria ELF32
little-endian dla platformy ARM-linux i mog� symulowa� wi�kszo��
test�w wydajno�ciowych SPEC Int i SPEC FP.

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .

%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/nwfpe.bin $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
