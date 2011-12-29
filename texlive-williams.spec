# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/williams
# catalog-date 2009-01-30 14:29:16 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-williams
Version:	20090130
Release:	1
Summary:	Miscellaneous macros by Peter Williams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/williams
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/williams.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/williams.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
