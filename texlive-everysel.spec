Name:		texlive-everysel
Version:	57489
Release:	2
Summary:	Provides hooks into \selectfont
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/everysel
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everysel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everysel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everysel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provided hooks whose arguments are executed just
after LaTeX has loaded a new font by means of \selectfont. It
has become obsolete with LaTeX versions 2021/01/05 or newer,
since LaTeX now provides its own hooks to fulfill this task.
For newer versions of LaTeX everysel only provides macros using
LaTeX's hook management due to compatibility reasons. See
lthooks-doc.pdf for instructions how to use lthooks instead of
everysel.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/everysel
%{_texmfdistdir}/tex/latex/everysel
%doc %{_texmfdistdir}/doc/latex/everysel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
