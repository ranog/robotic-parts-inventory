from datetime import date

from src.v2.allocation.domain.model import Batch, OrderLine


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch(ref='batch-001', sku=sku, qty=batch_qty, eta=date.today()),
        OrderLine(order_id='order-123', sku=sku, qty=line_qty),
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, line = make_batch_and_line(sku='STEPPER-MOTOR', batch_qty=20, line_qty=2)

    batch.allocate(line)

    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line(sku='STEPPER-MOTOR', batch_qty=20, line_qty=2)

    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line(sku='STEPPER-MOTOR', batch_qty=2, line_qty=20)

    assert not small_batch.can_allocate(large_line)


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line(sku='STEPPER-MOTOR', batch_qty=2, line_qty=2)

    assert batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch(ref='batch-001', sku='STEPPER-MOTOR', qty=20, eta=None)
    different_sku_line = OrderLine(order_id='order-ref', sku='MICRO-SERVO-9G-SG90', qty=2)

    assert batch.can_allocate(different_sku_line) is False


def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line(sku='STEPPER-MOTOR', batch_qty=20, line_qty=2)

    batch.deallocate(unallocated_line)

    assert batch.available_quantity == 20


def test_allocation_is_idempotent():
    batch, line = make_batch_and_line(sku='STEPPER-MOTOR', batch_qty=20, line_qty=2)

    batch.allocate(line)
    batch.allocate(line)

    assert batch.available_quantity == 18
