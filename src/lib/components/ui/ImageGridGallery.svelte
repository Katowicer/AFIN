<script lang="ts">
	import type { ElementProvider } from 'photoswipe';
	import PhotoSwipeLightbox from 'photoswipe/lightbox';
	import 'photoswipe/style.css';

	export type PhotoSwipeEntityImage = {
		src: string;
		alt?: string;
		width: number;
		height: number;
	};

	let { imgs } = $props<{ imgs: PhotoSwipeEntityImage[] }>();

	function PhotoSwipeEntity(galleryNode: ElementProvider | undefined) {
		const lightbox = new PhotoSwipeLightbox({
			gallery: galleryNode,
			children: 'a',
			pswpModule: () => import('photoswipe')
		});

		lightbox.init();
		return {
			destroy() {
				lightbox.destroy();
			}
		};
	}
</script>

<div class="grid grid-cols-1 gap-4 p-4 sm:grid-cols-2 md:grid-cols-3" use:PhotoSwipeEntity>
	{#each imgs as img}
		<a
			href={img.src}
			data-pswp-width={img.width}
			data-pswp-height={img.height}
			target="_blank"
			class="block overflow-hidden rounded-lg shadow-md transition-shadow hover:shadow-lg"
		>
			<img
				src={img.src}
				alt={img.alt ?? img.src}
				class="h-auto w-full transform object-cover shadow-black transition-all duration-1000 hover:scale-110 hover:shadow-2xl"
			/>
		</a>
	{/each}
</div>
