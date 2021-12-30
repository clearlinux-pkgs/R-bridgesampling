#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bridgesampling
Version  : 1.1.2
Release  : 44
URL      : https://cran.r-project.org/src/contrib/bridgesampling_1.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bridgesampling_1.1-2.tar.gz
Summary  : Bridge Sampling for Marginal Likelihoods and Bayes Factors
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Brobdingnag
Requires: R-coda
Requires: R-mvtnorm
Requires: R-scales
Requires: R-stringr
BuildRequires : R-Brobdingnag
BuildRequires : R-coda
BuildRequires : R-mvtnorm
BuildRequires : R-scales
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
factors, posterior model probabilities, and normalizing constants in general,
    via different versions of bridge sampling (Meng & Wong, 1996,

%prep
%setup -q -c -n bridgesampling
cd %{_builddir}/bridgesampling

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618587076

%install
export SOURCE_DATE_EPOCH=1618587076
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bridgesampling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bridgesampling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bridgesampling
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bridgesampling || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bridgesampling/CITATION
/usr/lib64/R/library/bridgesampling/DESCRIPTION
/usr/lib64/R/library/bridgesampling/INDEX
/usr/lib64/R/library/bridgesampling/Meta/Rd.rds
/usr/lib64/R/library/bridgesampling/Meta/data.rds
/usr/lib64/R/library/bridgesampling/Meta/features.rds
/usr/lib64/R/library/bridgesampling/Meta/hsearch.rds
/usr/lib64/R/library/bridgesampling/Meta/links.rds
/usr/lib64/R/library/bridgesampling/Meta/nsInfo.rds
/usr/lib64/R/library/bridgesampling/Meta/package.rds
/usr/lib64/R/library/bridgesampling/Meta/vignette.rds
/usr/lib64/R/library/bridgesampling/NAMESPACE
/usr/lib64/R/library/bridgesampling/NEWS
/usr/lib64/R/library/bridgesampling/R/bridgesampling
/usr/lib64/R/library/bridgesampling/R/bridgesampling.rdb
/usr/lib64/R/library/bridgesampling/R/bridgesampling.rdx
/usr/lib64/R/library/bridgesampling/data/Rdata.rdb
/usr/lib64/R/library/bridgesampling/data/Rdata.rds
/usr/lib64/R/library/bridgesampling/data/Rdata.rdx
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_jags.R
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_jags.Rmd
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_jags.html
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_nimble.R
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_nimble.Rmd
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_nimble.html
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_stan.R
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_stan.Rmd
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_example_stan.html
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_paper.pdf
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_paper.pdf.asis
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_paper_extended.pdf
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_paper_extended.pdf.asis
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_stan_ttest.R
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_stan_ttest.Rmd
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_stan_ttest.html
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_tutorial.pdf
/usr/lib64/R/library/bridgesampling/doc/bridgesampling_tutorial.pdf.asis
/usr/lib64/R/library/bridgesampling/doc/index.html
/usr/lib64/R/library/bridgesampling/extdata/vignette_example_jags.RData
/usr/lib64/R/library/bridgesampling/extdata/vignette_example_nimble.RData
/usr/lib64/R/library/bridgesampling/extdata/vignette_example_stan.RData
/usr/lib64/R/library/bridgesampling/extdata/vignette_stan_ttest.RData
/usr/lib64/R/library/bridgesampling/help/AnIndex
/usr/lib64/R/library/bridgesampling/help/aliases.rds
/usr/lib64/R/library/bridgesampling/help/bridgesampling.rdb
/usr/lib64/R/library/bridgesampling/help/bridgesampling.rdx
/usr/lib64/R/library/bridgesampling/help/paths.rds
/usr/lib64/R/library/bridgesampling/html/00Index.html
/usr/lib64/R/library/bridgesampling/html/R.css
/usr/lib64/R/library/bridgesampling/tests/testthat.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bf.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bridge_sampler.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bridge_sampler_Rcpp.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bridge_sampler_Rcpp_parallel.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bridge_sampler_mcmc.list.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bridge_sampler_parallel.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bridge_sampler_print_method.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-bridge_sampler_summary_method.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-nimble_bridge_sampler.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-post_prob.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-stan_bridge_sampler_basic.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-stan_bridge_sampler_bugs.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-stanreg_bridge_sampler_basic.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-vignette_example_jags.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-vignette_example_nimble.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-vignette_example_stan.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test-vignette_stan_ttest.R
/usr/lib64/R/library/bridgesampling/tests/testthat/test_dat.txt
/usr/lib64/R/library/bridgesampling/tests/testthat/unnormalized_normal_density.cpp
/usr/lib64/R/library/bridgesampling/tests/testthat/unnormalized_normal_density_mu.cpp
