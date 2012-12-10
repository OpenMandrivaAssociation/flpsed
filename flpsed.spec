# This spec is based on Astragalo's work in MIB

Name:		flpsed
Version:	0.7.0
Release:	%mkrel 2
Summary:	WYSIWYG pseudo PostScript editor
License:	GPLv2
Group:		Office
URL:		http://www.ecademix.com/JohannesHofmann/flpsed.html
Source:		http://www.ecademix.com/JohannesHofmann/%{name}-%{version}.tar.gz
Source1:	flpsed.desktop
Patch0:		flpsed-0.7.0-sfmt.patch
Requires:	ghostscript
Requires:	poppler
BuildRequires:	fltk-devel >= 1.3.0
BuildRequires:	pkgconfig(xft)
BuildRequires:	desktop-file-utils
BuildRequires:	lsb-build-base-devel
BuildRequires:	X11-devel


%description
Flpsed is a WYSIWYG pseudo PostScript editor. "Pseudo", because you can't
remove or modify existing elements of a document. Flpsed lets you add
arbitrary text lines to existing PostScript 1 documents. Added lines can later
be reedited with flpsed. Using pdftops, which is part of xpdf, one can convert
PDF documents to PostScript and also add text to them. flpsed is useful for
filling in forms, adding notes etc.

%prep
%setup -q
%patch0 -p1 -b .sfmt~

%build
%configure2_5x
%make


%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}%{_datadir}/applications
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/applications/*
%{_mandir}/man1/flpsed.1*



%changelog
* Tue Feb 28 2012 Andrey Bondrov <abondrov@mandriva.org> 0.7.0-2mdv2012.0
+ Revision: 781242
- Update BuildRequires
- imported package flpsed

