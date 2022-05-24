from hydraulics.hsystem import HSystem
from hydraulics.elements import Source, Tap, Sink, Split


def main():
    # create HSystem
    h_sys = HSystem()

    # create elements
    src_1 = Source("Source_1")
    tap_1 = Tap("Tap_1")
    spl_1 = Split("Split_1")
    snk_1 = Sink("Sink_1")
    snk_2 = Sink("Sink_2")

    # add elements to System
    h_sys.add_element(src_1)
    h_sys.add_element(tap_1)
    h_sys.add_element(spl_1)
    h_sys.add_element(snk_1)
    h_sys.add_element(snk_2)

    # get elements and print list of their names
    print("Elements in the system:")
    print([e.get_name() for e in h_sys.get_elements()])     # ['Source_1', 'Tap_1', 'Split_1', 'Sink_1', 'Sink_2']

    # connect elements
    src_1.connect(tap_1)
    tap_1.connect(spl_1)
    spl_1.connect_at(snk_1, 0)
    spl_1.connect_at(snk_2, 1)

    # get outputs
    print("Outputs:")
    print(src_1.get_output().get_name() if src_1.get_output() is not None else None)    # Tap_1
    print(tap_1.get_output().get_name() if tap_1.get_output() is not None else None)    # Split_1
    print([e.get_name() for e in spl_1.get_outputs() if e is not None])                 # ['Sink_1', 'Sink_2']

    # set simulation parameters
    src_1.set_flow(11.5)
    tap_1.set_status(to_open=True)

    # start simulation
    print("First simulation:")
    print(h_sys.simulate())
    # [
    #     'Source Source_1 0.000 11.500',
    #     'Tap Tap_1 11.500 11.500',
    #     'Split Split_1 11.500 5.750 5.750',
    #     'Sink Sink_1 5.750 0.000',
    #     'Sink Sink_2 5.750 0.000'
    # ]

    # close tap and run another simulation
    tap_1.set_status(to_open=False)
    print("Second simulation:")
    print(h_sys.simulate())
    # [
    #     'Source Source_1 0.000 11.500',
    #     'Tap Tap_1 11.500 0.000',
    #     'Split Split_1 0.000 0.000 0.000',
    #     'Sink Sink_1 0.000 0.000',
    #     'Sink Sink_2 0.000 0.000'
    # ]


if __name__ == "__main__":
    main()
