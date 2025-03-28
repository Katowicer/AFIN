<!--
<script lang="ts">
	import type { Snippet } from 'svelte';
	import NavBarLink from './NavBarLink.svelte';

	export type NavbarRoute = {
		href: string;
		content: Snippet | string;
	};

	let { routes } = $props<{ routes: NavbarRoute[] }>();
</script>

<nav
	class="flex justify-center bg-[#1E3A8A] py-4 text-white shadow-md"
	role="navigation"
	aria-label="Navigazione pagine"
>
	<ul class="flex-wrap space-x-4 px-5 sm:flex">
		{#each routes as route}
			<NavBarLink href={route.href}>{route.content}</NavBarLink>
		{/each}
	</ul>
</nav>
-->

<script lang="ts">
	import type { Snippet } from 'svelte';
	import NavBarLink from './NavBarLink.svelte';

	export type NavbarRoute = {
		href: string;
		content: Snippet | string;
	};

	let { routes } = $props<{ routes: NavbarRoute[] }>();

	let isOpen = $state(false);
	let toggleMenu = () => (isOpen = !isOpen);
</script>

<nav
	class="not-sm:flex-col justify-center bg-[#1E3A8A] py-4 text-white shadow-md sm:flex"
	role="navigation"
	aria-label="Navigazione pagine"
>
	<div class="flex items-center justify-between p-4 sm:hidden sm:p-0">
		<span class="px-2 font-serif text-lg font-thin">AFIN</span>
		<button
			aria-label="Toggle navigation menu"
			class="text-md rounded-md p-2 hover:bg-blue-900 focus:ring-2 focus:ring-yellow-400 sm:hidden"
			onclick={toggleMenu}
		>
			{#if isOpen}
				<span>✖</span> <!-- Close Icon -->
			{:else}
				<span>☰</span> <!-- Hamburger Icon -->
			{/if}
		</button>
	</div>

	<!-- Navigation Links -->

	<ul class="flex-wrap px-5 sm:flex sm:space-x-4" class:hidden={!isOpen}>
		{#each routes as route}
			<NavBarLink href={route.href}>{route.content}</NavBarLink>
		{/each}
	</ul>
</nav>
