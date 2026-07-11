%global tl_name williams
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Miscellaneous macros by Peter Williams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/williams
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/williams.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/williams.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides two packages: antree, which provides macros for
annotated node trees, and toklist, which is an implementation of Knuth's
token list macros, to be found on pp.378-379 of the TeXbook.

