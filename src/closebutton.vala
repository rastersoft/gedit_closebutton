using GLib;
using Gedit;
using Peas;
using Gtk;
using Gee;

namespace gedit_closebutton {

	public class Geditclosebutton : Gedit.WindowActivatable, Peas.ExtensionBase {

		private Gee.ArrayList<Gtk.HeaderBar> headerBars;

		public Geditclosebutton() {
			GLib.Object();
		}

		public Gedit.Window window {
			owned get; construct;
		}

		private void process_child(Gtk.Widget widget) {

			var element = widget as Gtk.HeaderBar;
			if (element != null) {
				if (element.show_close_button == false) {
					element.show_close_button = true;
					this.headerBars.add(element);
				}
				return;
			}

			var element2 = widget as Gtk.Container;
			if (element2 == null) {
				return;
			}
			foreach(var child in element2.get_children()) {
				this.process_child(child);
			}
		}

		public void activate () {
			this.headerBars = new Gee.ArrayList<Gtk.HeaderBar>();
			this.process_child(this.window);
		}

		public void deactivate () {
			foreach(var headerBar in this.headerBars) {
				headerBar.show_close_button = false;
			}
			this.headerBars = null;
		}

		public void update_state() {
		}
	}
}

[ModuleInit]
public void peas_register_types (TypeModule module) {
	var objmodule = module as Peas.ObjectModule;

	// Register my plugin extension
	objmodule.register_extension_type (typeof (Gedit.WindowActivatable), typeof (gedit_closebutton.Geditclosebutton));
}
