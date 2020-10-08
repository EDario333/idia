<template>
	<header class="header-global">
		<base-nav class="navbar-main" transparent type="" effect="light" expand>
			<router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
				<img src="img/brand/white2.png" alt="iDia"  />
			</router-link>

			<div class="row" slot="content-header" slot-scope="{closeMenu}">
				<div class="col-6 collapse-brand">
					<a href="#">
						<img src="img/brand/blue.png">
					</a>
				</div>

				<div class="col-6 collapse-close">
					<close-button @click="closeMenu"></close-button>
				</div>
			</div>

			<ul class="navbar-nav navbar-nav-hover align-items-lg-center">
				<li class="nav-item">
					<a href="#secCards" class="nav-link" role="button">
						<i class="ni ni-ui-04 d-lg-none"></i>
						<span class="nav-link-inner--text">
							{{ $t('sections.cards.title') }}
						</span>
					</a>
				</li>

				<li class="nav-item">
					<a href="/#secFeatures" class="nav-link" role="button">
						<i class="ni ni-ui-04 d-lg-none"></i>
						<span class="nav-link-inner--text">
							{{ $t('sections.features.title') }}
						</span>
					</a>
				</li>

				<base-dropdown tag="li" class="nav-item">
					<a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
						<i class="ni ni-collection d-lg-none"></i>
						<span class="nav-link-inner--text">
							{{ $t('sections.RDI.title') }}
						</span>
					</a>

					<a href="/#secRDI" class="dropdown-item">
						{{ $t('sections.RDI.what is') }}
					</a>

					<a href="/#secTech" class="dropdown-item">
						{{ $t('sections.tech.title') }}
					</a>
				</base-dropdown>

				<li class="nav-item">
					<a href="/#secServices" class="nav-link" role="button">
						<i class="ni ni-ui-04 d-lg-none"></i>
						<span class="nav-link-inner--text">
							{{ $t('sections.services.title') }}
						</span>
					</a>
				</li>

				<li class="nav-item">
					<a href="/#secContact" class="nav-link" role="button">
						<i class="ni ni-ui-04 d-lg-none"></i>
						<span class="nav-link-inner--text">
							{{ $t('sections.contact.title') }}
						</span>
					</a>
				</li>
			</ul>

			<ul class="navbar-nav align-items-lg-center ml-lg-auto">
				<li class="nav-item">
					<a
						class="nav-link nav-link-icon"
						href="https://twitter.com/EdgarRa90028538"
						target="_blank"
						rel="noopener"
						data-toggle="tooltip"
						:data-original-title="$t('Follow me on Twitter')"
            :title="$t('Follow me on Twitter')"
					>
						<i class="fa fa-twitter-square"></i>
						<span class="nav-link-inner--text d-lg-none">
							Twitter
						</span>
					</a>
				</li>

				<li class="nav-item">
					<a
						class="nav-link nav-link-icon"
						href="https://github.com/EDario333"
						target="_blank"
						rel="noopener"
						data-toggle="tooltip"
						:data-original-title="$t('Star me on Github')"
            :title="$t('Star me on Github')"
					>
						<i class="fa fa-github"></i>
						<span class="nav-link-inner--text d-lg-none">
							Github
						</span>
					</a>
				</li>
			</ul>
		</base-nav>
	</header>
</template>

<script>
	import BaseNav from "@/components/BaseNav";
	import BaseDropdown from "@/components/BaseDropdown";
	import CloseButton from "@/components/CloseButton";

	export default {
		components: {
			BaseNav,
			CloseButton,
			BaseDropdown
		}
	};
</script>

<style>
</style>
