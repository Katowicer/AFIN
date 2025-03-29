<script lang="ts">
	import '../app.css';
	import Navbar, { NavbarRoute } from '../lib/components/ui/Navbar/Navbar.svelte';

	let { children } = $props();
	const routes: NavbarRoute[] = [
		{ href: '/', content: 'Home' },
		{ href: 'history', content: 'Storia' },
		{ href: 'activity', content: 'Attività' },
		{ href: 'finality', content: 'Finalità' },
		{ href: 'voices', content: 'La voce dei protagonisti' },
		{ href: 'docs', content: 'Documenti' },
		{ href: 'news', content: 'News' },
		{ href: 'gallery', content: 'Galleria' },
		{ href: 'contacts', content: 'Contatti' },
		{ href: 'donate', content: 'Per donare' }
	];
</script>

<div class="flex min-h-screen flex-col text-sm sm:text-base md:text-lg">
	<Navbar {routes} />

	<main
		class="mx-auto mb-4 max-w-4/5 grow flex-col space-y-10 p-4 text-justify text-sm sm:text-base md:p-6 md:text-lg lg:max-w-5/6 lg:p-6 xl:max-w-3/4 2xl:max-w-1/2"
	>
		{@render children()}
	</main>

	<footer class="mt-auto w-full bg-[#1E3A8A] py-4 text-center text-white">
		<p>&copy; 2025 Afin Associazione Famiglie Ipo Non Vedenti. All rights reserved.</p>
	</footer>
</div>
