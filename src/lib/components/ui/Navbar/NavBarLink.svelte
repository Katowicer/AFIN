<script lang="ts">
	import type { Snippet } from 'svelte';
	import { page } from '$app/state';

	export type NavRoute = { href: string };
	let { href, children } = $props<{ href: string; children: Snippet }>();
</script>

<a
	class="mt-2 flex p-2 shadow-xs shadow-black transition-all
           duration-300 ease-in-out
           hover:rounded-md hover:bg-[#0c193e] hover:underline focus:ring-yellow-400"
	{href}
	aria-current={page.url.pathname === href ? 'page' : undefined}
	aria-label={`Naviga alla pagine ${href}`}
>
	{@render children?.()}
</a>
