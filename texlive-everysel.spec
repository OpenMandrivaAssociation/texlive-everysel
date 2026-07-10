%global tl_name everysel
%global tl_revision 57489

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Provides hooks into \selectfont
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/everysel
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everysel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everysel.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everysel.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provided hooks whose arguments are executed just after LaTeX
has loaded a new font by means of \selectfont. It has become obsolete
with LaTeX versions 2021/01/05 or newer, since LaTeX now provides its
own hooks to fulfill this task. For newer versions of LaTeX everysel
only provides macros using LaTeX's hook management due to compatibility
reasons. See lthooks-doc.pdf for instructions how to use lthooks instead
of everysel.

