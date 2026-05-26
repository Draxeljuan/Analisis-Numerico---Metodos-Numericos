import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MetodosNumericosComponent } from './metodos-numericos.component';

describe('MetodosNumericosComponent', () => {
  let component: MetodosNumericosComponent;
  let fixture: ComponentFixture<MetodosNumericosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MetodosNumericosComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MetodosNumericosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
