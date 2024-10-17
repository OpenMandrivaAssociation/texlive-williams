Name:		texlive-williams
Version:	15878
Release:	2
Summary:	Miscellaneous macros by Peter Williams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/williams
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/williams.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/williams.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides two packages: - antree, which provides
macros for annotated node trees, and - toklist, which is an
implementation of Knuth's token list macros, to be found on
pp.378-379 of the TeXbook.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/williams/antree.sty
%{_texmfdistdir}/tex/latex/williams/toklist.sty
%doc %{_texmfdistdir}/doc/latex/williams/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
