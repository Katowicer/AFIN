<script lang="ts">
	import { base } from '$app/paths';
	import '../app.css';
	import Navbar, { type NavbarRoute } from '../lib/components/ui/Navbar/Navbar.svelte';

	let { children } = $props();
	const routes: NavbarRoute[] = [
		{ href: base + '/', content: 'Home' },
		{ href: base + '/history', content: 'Storia' },
		{ href: base + '/activity', content: 'Attività' },
		{ href: base + '/finality', content: 'Finalità' },
		{ href: base + '/voices', content: 'La voce dei protagonisti' },
		{ href: base + '/docs', content: 'Documenti' },
		{ href: base + '/news', content: 'News' },
		{ href: base + '/gallery', content: 'Galleria' },
		{ href: base + '/contacts', content: 'Contatti' },
		{ href: base + '/donate', content: 'Per donare' }
	];
</script>

<div class="flex min-h-screen flex-col text-base sm:text-base md:text-lg">
	<Navbar {routes} />

	<main
		class="mx-auto mb-4 sm:max-w-4/5 grow flex-col space-y-10 p-4 text-justify text-sm sm:text-base md:p-6 md:text-lg lg:max-w-5/6 lg:p-6 xl:max-w-3/4 2xl:max-w-1/2"
	>
		{@render children()}
	</main>

	<footer class="mt-auto w-full bg-[#1E3A8A] py-4 text-center text-white">
		<p>&copy; 2025 Afin Associazione Famiglie Ipo Non Vedenti. All rights reserved.</p>
	</footer>
</div>
